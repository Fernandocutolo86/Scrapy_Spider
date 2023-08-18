import pytest
from scrapy.http import TextResponse
from spider_teste_Shida import spider_teste_Shida

@pytest.fixture
def fake_response():
    with open('fake_response.html', 'r', encoding='utf-8') as f:
        content = f.read()
    response = TextResponse('http://quotes.toscrape.com/page/1/', body=content.encode('utf-8'))
    return response

def test_quotes_spider(fake_response):
    spider = spider_teste_Shida()
    spider.page_number = 1
    results = list(spider.parse(fake_response))
    
    assert len(results) == 2
    assert results[0]['rule_number'] == 1
    assert results[1]['rule_number'] == 2

# Pode adicionar mais testes se achar necessário





