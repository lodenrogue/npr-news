from newspaper import Article
from model.content import Content

SNIPPET_LENGTH = 200
NPR_PREFIX = "NPR >"

class NprContentExtractor:

    def extract(self, url):
        snippet = self._get_snippet(url)
        return Content(snippet)


    def _get_snippet(self, url):
        article = Article(url)
        article.download()
        article.parse()
        
        text = article.text
        if text is None:
            return ""
        
        text = self._clean_text(text)
        if len(text) < SNIPPET_LENGTH:
            return text

        return text[0:SNIPPET_LENGTH].rstrip() + "..."


    def _clean_text(self, text):
        result = ""
        for line in text.split('\n'):
            if not line.startswith(NPR_PREFIX):
                result += line.replace("\n", " ")
       
        return result        
