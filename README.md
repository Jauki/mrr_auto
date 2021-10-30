# Monthly Reading Requirement Auto ⚙️

 A tool to help you do the monthly reading requirements



## Important ⚠️

+ **Some words can't be translated**
+ Links:
  + [Synonym / Explaination](thesaurus.yourdictionary.com/)
  + [Sentence](https://sentence.yourdictionary.com/)
  + [googletrans](https://pypi.org/project/googletrans/)
    + I used the version 3.1.0a0 (the other libraries work fine)
    + `pip install googletrans==3.1.0a0`



## Usage 📝

How to use it:

+ **paste** your words in the in.txt file

+ **!please!** make sure to format it like this:

  ```txt 
  word1
  word2
  word3
  word4
  ...
  ```

+ the final product will be in the `out.md` , it will be formated in a markdown table like this:

  | word | sentence | explanation | german |
  | ---- | -------- | ----------- | ------ |
  |      |          |             |        |
  |      |          |             |        |
  |      |          |             |        |



## How it's done! 💽

Basically the word will be translated via the [googletrans](https://pypi.org/project/googletrans/) API, really easy to use and for the sentence and explanation I didn't find a API, so scrapped it from the Web via [BeatifulSoup4](https://pypi.org/project/beautifulsoup4/). 
