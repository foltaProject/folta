## Working with the OPUS Tool

In order to access the JW300 corpus, you must use the opustools package.
##### FOLTA Virtual Environment
To use opus tools, you must be in the virtual environment on Awakateko.

```
$ source /projects/folta/envs/folta/bin/activate
```
Note: This particular command can be run in this format from anywhere on Awakateko. 
The path is absolute and does not need to be changed to reflect your current location.
##### Terminal Opus Query
Next, you will need to run the `opus_read` command to query the API for the bi-text.
```
$ opus_read -d JW300 -s af -t bg -wm moses -w jw300.af jw300.bg
```
There are a lot of flags here, so let's break them down.

`-d JW300` -- corpus name - If you are looking to query the JW300 corpus, leave this as JW300.
If we start to work with other texts from OPUS, you'll want to change this to correspond
to the relevant corpus within OPUS.
 
`-s af` -- source language ID - This is the language code for the source language.
In this case, `af` for `Afrikaans`. 
A full list of languages and abbreviations can be found in the JW300 github directory, 
in the `languages.json` file.
 
`-t bg` -- target language ID - This is the language code for the source language.
In this case, `bg` for `Bulgarian`.
 
`-wm moses` -- write mode (normal,moses,tmx,links) - I have not experimented with these.
I can honestly say that I don't know the differences.
 
`-w jw300.af jw300.bg` -- Write to file - Filename to write bi-text to.
"To print moses format in separate files, enter two file names. Otherwise enter one file name." - OPUS Documentation.
Apparently, the Moses write mode is the only one that _can_ be written out to two files, 
but it might not be required. 
When you do so, it appears that the source text is first, followed by the target text.

##### Python OPUS Query
It appears as though you can also query opus from within a python script.

```python
# import the module
import opustools_pkg 
```
Next, we instantiate the OPUS reader object.
```python
# instantiate the opus reader object
opus_reader = opustools_pkg.OpusRead(
    directory='JW300',
    source='en',
    target='fi')
```
Finally, we print out the texts. 
The documentation is sparse, but I'm not sure this part is working properly. 
For me, it tried to query a certain link, but it looks like where the data is stored has changed and no corresponding change has been made to the tool. 
However, you still get links (whether run in jupyter or terminal) to the proper text, but you have to manually click them, open them, unzip them, etc. 
It doesn't seem as though there is a straightforward way to stream them into a script or process, yet.
```
# print out the available texts
opus_reader.printPairs()
```