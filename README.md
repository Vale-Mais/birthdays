# Implementation of a Database of Birthdays

Birthdays is a projects that takes users' inputs from the a machine terminal, checks whether or not 
there is the corresponding birthday inside of an internal csv database and, if needed, it can let the user add them directly 
inside the database.

## Installation

Use the command `git clone https://github.com/Vale-Mais/birthdays` in the command prompt
of your PC in order to automatically download the whole folder containing the modules.
Git should have been previously installed on the machine.

## Usage

If wanting the execute the program, the command should be written as follows:

```bash
python main.py "name"
```

Whereas "name" should be the name of a known person. 
For example:

```bash
python main.py "Albert Einstein"
```

In this case, since the name is in the database, the output will be:

```bash
The birthday of  Albert Einstein is  03/14/1879
```

To do so, people's names and corresponding birthdays have been added to a database. 

To increase the speed of interaction, the user can access the shortcut `-a` thanks to `argparse`.
This command allows you to skip a step and add a new person and birthday directly to the database by simply writing the -a keyword next to the new name to add.

```bash
python main.py "Justin Timberlake" -a
```

An another useful optional argument is `-h`; this gives the user some help about the functioning and the rules of the code.

The output in this case will be:

```bash
usage: main.py [-h] [-a] name

this program will check if the name you put is inside our database of known people
or their birthday. If the names have more than one space, wrap them around quotes
("")

positional arguments:
  name        input the name of a known person or birthday

optional arguments:
  -h, --help  show this help message and exit
  -a, --add   add a new guitarist or band
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
