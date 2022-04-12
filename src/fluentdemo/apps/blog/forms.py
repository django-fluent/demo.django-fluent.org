from fluent_comments.forms import CompactLabelsCommentForm


class CommentForm(CompactLabelsCommentForm):
    """
    The comment form to use
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fix translations of the labels
        self.fields['url'].label = "Website"
