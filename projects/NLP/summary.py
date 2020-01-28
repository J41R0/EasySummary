def get_summary(n_ideas, opinions):
    """
    Get the most n important ideas from a set of opinions
    Args:
        n_ideas: desired number of most important ideas
        opinions: dict format opinions in way:  {"opinions":[{"id":<op_id>, "text":<op_text>},...]}

    Returns: The n most important ideas in a single string

    """

