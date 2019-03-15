def serialize(post):

    serialized_post = serialize_id(post)

    serialized_post.update({
        'subject': post.subject,
        'content': post.content
    })

    return serialized_post


def serialize_id(post):
    return {
        'id': post.id
    }
