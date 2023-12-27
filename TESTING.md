# Testing

Return back to the [README.md](README.md) file.

## Code Validation

![CODE VALIDATION](documentation/test-bug1.png)

### Python

The CI Python Linter can be used two different ways.
- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click on.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).
    - Check the example table below for a live demo.

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp3-mastermind-2023/main/run.py) | ![screenshot](documentation/test-bug1.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Brave | Safari  | Edge | Firefox |
| --- | --- | --- | --- |
| ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-about.png) |  ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-about.png) | 

## Responsiveness

Is this needed? 
I have nothing with heroku to do?

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| ![screenshot](documentation/responsive-4k-about.png) | ![screenshot](documentation/responsive-4k-contact.png) | ![screenshot](documentation/responsive-4k-etc.png) | Noticeable scaling issues |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| --- | Non valid color option should prompt a message | --- | It does | --- | ![screenshot](documentation/test-error-letter.png)

The use of Simple_term_menu minimized the possibility for input errors. 



## Bugs

- I found this bug, but only sometimes when returning from the rules screen. 
    not every time, just when I spammed rules and return a couple of times.
    It´s NOT the prettiest fix, but it worked. 

    ![screenshot](documentation/test-error-lvlsrtrn.png)

    - To fix this, I made changes to the lines below. 
    elif menu_entry_index == 1:
        tries, code_length = display_levels()
        if tries is not None and code_length is not None:
            game(tries, code_length)

    - This is the main menu entry. I added the "None" parts, and added:
    elif level_entry_index == 3:
        print_welcome_message()
        return None, None
    
- This bug happened after I had changed the way TRIES and CODE_LENGTH 
    worked, at some places I still tried to use the old Constants. After 
    the change for using menu entries to determine # tries and code length 
    I had to remove every instance of TRIES in the code.

    ![screenshot](documentation/test-error-tries2.png)
    
    - Fixes were to remove all mentions of TRIES as a constant, and use lowercase
    
    
    
- This I thought was of the same kind as the TRIES one, it kinda was, but it tried to read the correct/incorrect_pos, that threw me off. It was I who still tried to talk to two unexisting constants, and then tried to read the lists with zip that gave me errors. 

    ![screenshot](documentation/test-error3.png)

    - Change of names fixed it. I found [this](https://www.freecodecamp.org/news/typeerror-cannot-unpack-non-iterable-nonetype-object-how-to-fix-in-python/), but it wasn't really the solution. Just a symptom of the problem. 


## Unfixed Bugs

There are no remaining bugs that I am aware of.

