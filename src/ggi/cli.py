import os

import click

from ggi.helpers import (
    check_lang_support,
    convert_list_to_str,
    get_available_langs,
    get_gitignore,
    sanity_check_lang,
    write_gitignore,
)
from ggi.supported_langs import SUPPORTED_LANGS


@click.group(invoke_without_command=True)
@click.option(
    "--lang",
    "-l",
    help="Specify the language to generate a .gitignore for.",
    type=click.Choice(SUPPORTED_LANGS, case_sensitive=False),
)
@click.option(
    "--dir",
    "-d",
    default=".",
    help="Specify the directory to generate the .gitignore file in.",
)
@click.option(
    "--overwrite",
    "-ow",
    is_flag=True,
    help="Overwrites the existing .gitignore file if it exists.",
)
@click.pass_context
def main(ctx: click.Context, lang: str, dir: str, overwrite: bool) -> None:
    if ctx.invoked_subcommand is None:
        gen(lang, dir, overwrite)


def gen(lang: str, dir: str, overwrite: bool) -> None:
    os.makedirs(dir, exist_ok=True)

    lang_ok = sanity_check_lang(lang)
    if lang_ok is None:
        click.echo(f"Error: {lang} is not supported")
        return

    gitignore = get_gitignore(lang_ok)
    write_gitignore(dir, overwrite, gitignore)

    click.echo("Done!")


@main.command("ls", help="List supported languages as of 4/24/2025 PT.")
def ls() -> None:
    langs = convert_list_to_str(SUPPORTED_LANGS)
    click.echo(langs)


@main.command(
    "ls-remote",
    help="List supported languages in real-time.",
)
def ls_remote() -> None:
    ls = get_available_langs()
    langs = convert_list_to_str(ls)
    click.echo(langs)


@main.command("check", help="Check if the specified language is supported.")
@click.argument("lang")
def check(lang: str) -> None:
    lang_ok = check_lang_support(lang)
    msg = "Supported" if lang_ok else "Not supported"
    click.echo(msg)


@main.command(
    "check-remote",
    help="Check if the specified language is supported in real-time.",
)
@click.argument("lang")
def check_remote(lang: str) -> None:
    lang_ok = check_lang_support(lang, True)
    msg = "Supported" if lang_ok else "Not supported"
    click.echo(msg)
