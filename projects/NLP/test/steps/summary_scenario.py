import json
from behave import given, when, then
from projects.NLP.summary import get_summary


@given(u'I have enterd the number of expected n_ideas {n_ideas}')
def def_num_ideas(context, n_ideas):
    context.n_ideas = int(n_ideas)


@given(u'I also input a list of opinions {opinions} to summarizer')
def def_opinions(context, opinions):
    context.opinions = json.loads(opinions)


@when(u'I call the function get_summary')
def call_get_opinions(context):
    context.result = get_summary(context.n_ideas, context.opinions['opinions'])


@then(u'I get result {result}')
def test_results(context, result):
    assert context.result == result
