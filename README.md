<!-- hide -->
<div align="center">

# Learn Python Functions Interactively

![Certified by 4Geeks Academy](https://img.shields.io/badge/certified%20by-4Geeks%20Academy-2563eb) ![Auto-graded with LearnPack](https://img.shields.io/badge/auto--graded-LearnPack-2563eb) [![Open in GitHub Codespaces](https://img.shields.io/badge/open%20in-GitHub%20Codespaces-fb5a1f?logo=github&logoColor=white)](https://codespaces.new/?repo=4GeeksAcademy/python-functions-programming-exercises)

</div>

*These instructions are also available in [🇪🇸 Spanish](https://github.com/4GeeksAcademy/python-functions-programming-exercises/blob/HEAD/README.es.md).*
<!-- endhide -->

This LearnPack tutorial teaches Python functions through 10 interactive exercises: one welcome page plus 9 auto-graded challenges. You will print your first line on the console, define and call functions, write lambda expressions, chain the return value of one function into another, build a function with five parameters and sort a list of names. Each graded exercise ships a pytest file and a video walkthrough, in English and Spanish. Estimated time: 10 hours.

<!-- hide -->
## 📋 About this tutorial

- **Difficulty:** easy (beginner level, right after Python basics).
- **Estimated duration:** 10 hours.
- **Exercises:** 10 folders — 1 welcome page and 9 graded exercises.
- **Technologies:** Python 3, pytest, LearnPack.
- **Grading:** automatic, 9 exercises with a pytest file and 39 individual tests in total.
- **Extras:** a YouTube walkthrough linked from every exercise and a hidden `solution.hide.py` in each graded exercise.
- **Languages:** English and Spanish (every exercise has `README.md` and `README.es.md`).

![Cover badge of the Python Functions Tutorial: a cream-coloured card with the words PYTHON FUNCTIONS TUTORIAL, the blue and yellow Python logo, and a black footer that reads TIME TO CODE](https://raw.githubusercontent.com/4GeeksAcademy/python-functions-programming-exercises/master/python-functions-badge.png)
<!-- endhide -->

## 🎯 What will you learn?

The tutorial goes from the very first `print()` to functions that feed other functions, one small step at a time:

- How to declare a function with `def`, name its parameters and indent its body correctly.
- The difference between **defining** a function and **calling** it, and why nothing happens until you call it.
- How `return` works, and why a function that returns a value is more useful than one that only prints.
- How to write **lambda functions**: one-line, anonymous functions stored in a variable or passed around as arguments.
- How to combine functions, using the output of one as the input of the next.
- How to design a function with several parameters and pick names that explain themselves.
- How to use built-in list helpers such as `sorted()` inside your own function.

## 👀 What will you build?

Nine graded exercises, each one a tiny Python program you complete inside `app.py`:

1. **`01` Hello World** — use `print()` to display exactly `Hello World` on the console.
2. **`02` What is a function?** — reuse the `sum(number1, number2)` function you are given to store the result of `3445324 + 53454423` in a variable called `super_duper`.
3. **`03` Calling a function** — call the `calculate_area(length, width)` function you are given three times and store the area of each square in `square_area1`, `square_area2` and `square_area3`: 16, 4 and 25.
4. **`04` Defining vs. calling a function** — define `multi` from scratch so it receives two numbers and returns their multiplication.
5. **`05` Lambda functions** — assign a lambda to `is_odd` that returns `True` when a number is odd and `False` when it is not.
6. **`06` Lambda functions II** — assign a lambda to `rapid` that returns a string without its last character, so `"maria"` becomes `"mari"`.
7. **`07` Functions that return** — chain the two converters you are given, `dollar_to_euro` and `euro_to_yen`, to print how much 137 dollars are worth in yen: `20159.139`.
8. **`08` Function parameters** — build `render_person` with five parameters so it returns a sentence like `Bob is a 23 years old male born in 05/22/1983 with green eyes`.
9. **`09` List methods** — write `sort_names` so that, given a list of names, it returns them in alphabetical order.

The tenth folder, `00-Welcome`, is the introduction: no code, no test, just the roadmap and the intro video.

## 🎓 What do you need before starting?

- **Python fundamentals only.** Variables, numbers, strings and `print()` are enough; functions are exactly what this tutorial teaches you.
- **A browser**, if you run it on GitHub Codespaces or on the online platform. Nothing to install.
- **Python 3 and Node.js 14+**, only if you prefer to run the exercises on your own machine with LearnPack.
- **No previous experience with pytest.** The tests are already written; you only read their messages.

## ✅ How does the automatic grading work?

Each of the 9 graded exercises includes a test file written with pytest (`test.py` in exercises `01` and `07`, `tests.py` in the rest). When you press the compile or test button, LearnPack runs those assertions against your `app.py` and shows you a green or red line per check, with the message declared in `@pytest.mark.it(...)`, for example *"The function multi must receive two numbers and return their multiplication"*.

The tests verify three different things, and it helps a lot to know which one is failing:

- **The source code of `app.py`**, matched with a regular expression. Exercise `05` literally searches for `is_odd = lambda`, and exercise `03` checks that somewhere in your file you write `= calculate_area(`.
- **The value your function returns**, by importing it and calling it with fixed inputs, such as `app.multi(3, 4) == 12` or `app.calculate_area(5, 4) == 20`.
- **The text printed on the console**, captured and compared character by character, such as `"20159.139\n"` in exercise `07`.

The tests are deliberately strict, so treat a red line as a hint about the exact wording or the exact syntax being asked for, not as a verdict on your logic.

## 💡 What mistakes should you avoid?

- **Printing when the exercise asks you to return.** In `08` the test calls `render_person('ax','b','c','d','e')` and compares the returned string, while `app.py` already prints the result. A function that prints and returns nothing fails.
- **Getting the parameter order wrong in `08`.** The expected sentence is `ax is a d years old e born in b with c eyes`, so the five parameters go in this order: name, birth date, eye colour, age, gender.
- **Using `def` where a lambda is required.** In `05` and `06` the test reads your file looking for `is_odd = lambda` and `rapid = lambda`. A regular `def` fails the check even when the behaviour is correct.
- **Returning `list.sort()` in `09`.** The `sort()` method sorts in place and returns `None`. Return `sorted(names)` instead, and keep the `print(sort_names(names))` line, because the test compares the console output with `['Bob', 'Dilan', 'John', 'Kenny', 'Tom']`.
- **Formatting or rounding the number in `07`.** The console must show exactly `20159.139`: call `dollar_to_euro(137)` first and pass its result to `euro_to_yen`, without touching the decimals.
- **Deleting the code you are given.** Exercise `02` needs the `sum()` function it hands you, because the test imports it. In `04`, `06`, `08` and `09` the lines marked as "do not change" call your function with fixed values, and in `09` the test reads exactly what that line prints.

## ❓ Frequently asked questions

### Do I need to install Python to start the exercises?

No. Opening the repository in GitHub Codespaces gives you a ready environment with Python, LearnPack and the exercises already loaded, and the same tutorial also runs on the online platform. Installing anything locally is optional and only requires Python 3 and Node.js 14 or higher.

### What is the difference between `def` and a lambda function in Python?

A function declared with `def` has a name, can span as many lines as you need and returns a value only when you write `return`. A [lambda](https://docs.python.org/3/reference/expressions.html#lambda) is a single expression with no name of its own, usually stored in a variable such as `is_odd = lambda num: num % 2 != 0`, and it returns the result of that expression automatically. Exercises `04` to `06` make you write both styles for the same kind of problem.

### How long does this Python functions tutorial take?

The package is estimated at 10 hours and rated as easy. Its 9 graded exercises are short, so many people finish them in a couple of sessions; the time also depends on how much you experiment with the code beyond what the test asks for.

### Are these exercises free, and can I reuse them?

Access does not cost anything, and the code you write inside `app.py` is yours. The tutorial content, however, is not open source: the [LICENSE.md](https://github.com/4GeeksAcademy/python-functions-programming-exercises/blob/HEAD/LICENSE.md) file of this 4Geeks Academy tutorial reserves all intellectual property rights and does not allow you to republish, sell, sub-license or redistribute the material.

### Why does my exercise fail when the result looks right?

Because most checks compare strings exactly. A missing capital letter in `Hello World`, an extra space, a rounded decimal or a `def` where a lambda was requested is enough to turn the check red. Read the sentence next to the failing test: it names the function, the input and the value expected.

### Are the exercises available in Spanish?

Yes. All 10 folders ship both `README.md` and `README.es.md`, so instructions, hints and examples are fully translated, and the tutorial is published in Spanish as well. The code, the function names and the test messages stay in English, as they do in real projects.

<!-- hide -->
## 📚 Related tutorials

If you want to keep practising Python with the same interactive, auto-graded format:

1. [Learn Python Interactively (beginner)](https://4geeks.com/en/interactive-exercise/python-beginner-exercises) — variables, conditionals and the basics you need before this tutorial.
2. [Learn Python Loops and Lists Interactively](https://4geeks.com/en/interactive-exercise/python-loops-lists-exercises) — the natural next step after functions.
3. [Learn Object Oriented Programming with Python](https://4geeks.com/en/interactive-exercise/object-oriented-programing-with-python) — classes, objects and methods.
4. [Master Python by practice](https://4geeks.com/en/interactive-exercise/master-python-exercises) — a longer set of challenges to consolidate everything.
5. [Working with Functions in Python](https://4geeks.com/lesson/working-with-functions-python) — the written lesson behind these exercises.

## 🚀 How to start

The fastest way is one click: [Open in Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-functions-programming-exercises) (recommended) or [Open in Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/python-functions-programming-exercises).

Once VS Code opens, the LearnPack exercises should start on their own. If they do not, type `learnpack start` in the terminal.

![Animated preview of the LearnPack tutorial running inside VS Code: the code editor with app.py on the left and the exercise instructions with Previous and Next buttons on the right](https://raw.githubusercontent.com/4GeeksAcademy/python-functions-programming-exercises/master/preview.gif)

## 💻 Local installation

1. Install [LearnPack](https://learnpack.co) and its Python plugin. You need Node.js 14+ and Python 3+ first.

   ```bash
   npm i -g @learnpack/learnpack@2.1.20 && learnpack plugins:install @learnpack/python@1.0.0
   ```

2. Clone or download this repository into your local environment.

   ```bash
   git clone https://github.com/4GeeksAcademy/python-functions-programming-exercises.git
   cd python-functions-programming-exercises
   ```

3. Install the testing dependencies and start the tutorial from the root of the project.

   ```bash
   pip3 install pytest==6.2.5 pytest-testdox mock
   learnpack start
   ```

Once the download finishes you will find an `exercises` folder containing all the exercises.

## 📝 How the exercises are organized

Every graded exercise is a small Python application with the same files:

1. **`app.py`** — the entry file you edit and the one the computer runs.
2. **`README.md`** and **`README.es.md`** — the instructions, hints and the video walkthrough, in both languages.
3. **`test.py`** or **`tests.py`** — the grading script. You do not need to open it, but reading it is the fastest way to understand what is being asked.
4. **`solution.hide.py`** — a reference solution that LearnPack keeps hidden while you work.

## 🤝 Contributors

Thanks to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — coder 💻, idea 🤔, build-tests ⚠️, pull-request-review 👀, build-tutorial ✅, documentation 📖.
2. [Paolo (plucodev)](https://github.com/plucodev) — bug reports 🐛, coder 💻, translation 🌎.
3. [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo) — bug reports 🐛, translation 🌎.

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind are welcome: if you find a bug or a misspelling, [open an issue](https://github.com/learnpack/learnpack/issues/new) or send a pull request. See [all contributors](https://github.com/4GeeksAcademy/python-functions-programming-exercises/graphs/contributors).

This and many other exercises are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp), led by [Alejandro Sánchez](https://github.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer) and our [Data Science and Machine Learning Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).
<!-- endhide -->
