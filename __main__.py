#python3

import typer
import mdpre 

app = typer.Typer()


@app.command()
def mdpre(input_file : typer.FileText, output_file : typer.FileTextWrite, verbose: bool = False):
    typer.echo(f"mdpre {input_file} {output_file}")

    data_in = input_file.read()
    if verbose:
        print(data_in)
    else:
        print('mdpre!')
    output_file.write(data_in)

@app.command()
def md2pptx(input_file : typer.FileText, output_file : typer.FileTextWrite, pre : bool = False, verbose: bool = False):
    data_in = input_file.read()

    if pre:
        with open(input_file.name.replace('.mdp', '.md'), 'w') as processed_md:
            mdpre(input_file,processed_md)

    if verbose:
        typer.echo(f"md2pptx {input_file} {output_file}")
        print(data_in)

    else:
        typer.echo(f"md2pptx!")

    output_file.write(data_in)


if __name__ == "__main__":
    app()
