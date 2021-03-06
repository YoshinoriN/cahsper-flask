import json
from flask import Blueprint, Response
from cahsper.models.comments import Comments
from cahsper.utils.logger import http_request_logging

module_comments = Blueprint('comments', __name__)

@module_comments.route("/comments", methods=['GET'], strict_slashes=False)
@http_request_logging
def get_comments():
    comments = []
    for comment in Comments.get_all():
        comments.append(comment.serialize())

    return Response(response=json.dumps(comments), status=200, content_type='application/json')
