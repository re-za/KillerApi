db = {
    'users': [
        {
            'username': "reza",
            'name': "Reza Mousavi",
            'avatar': "/static/user_images/beard.png",
            'cover': "/static/user_images/flowers.jpg",
            'location': "Paris, FR",
            'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam laoreet sagittis vulputate. Cras quam urna, tincidunt vel augue id, eleifend ultrices velit.'
        },
        {
            'username': "anne",
            'name': "Anne",
            'avatar': "/static/user_images/spiderwoman.png",
            'cover': "/static/user_images/fly.jpg",
            'location': "London, UK",
            'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam laoreet sagittis vulputate. Cras quam urna, tincidunt vel augue id, eleifend ultrices velit.'
        },
        {
            'username': "paul",
            'name': "Paul",
            'avatar': "/static/user_images/dr-who.png",
            'cover': "/static/user_images/balloons.jpg",
            'location': "London, UK",
            'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam laoreet sagittis vulputate. Cras quam urna, tincidunt vel augue id, eleifend ultrices velit.'
        },
        {
            'username': "kenn",
            'name': "Ken",
            'avatar': "/static/user_images/kenn.png",
            'cover': "/static/user_images/balloons.jpg",
            'location': "London, UK",
            'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam laoreet sagittis vulputate. Cras quam urna, tincidunt vel augue id, eleifend ultrices velit.'
        },
        {
            'username': "sara",
            'name': "Sarah",
            'avatar': "/static/user_images/sara.png",
            'cover': "/static/user_images/fly.jpg",
            'location': "London, UK",
            'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam laoreet sagittis vulputate. Cras quam urna, tincidunt vel augue id, eleifend ultrices velit.'
        }
    ],
    'posts': [
        {
            'id': '111',
            'rawPost': "reza's post 1 ** This is a message",
            'title': "reza's post 1",
            'text': "This is a message",
            'link': None,
            'timestamp': 1504104583,
            'author': 'reza',
            'replyToId': None,
        },
        {
            'id': '112',
            'rawPost': "Reza Post 2 ** This is another message https://d3n8a8pro7vhmx.cloudfront.net/taxpayers/pages/679/attachments/original/1499663166/4-ways-cheer-up-depressed-cat.jpg",
            'title': "Reza Post 2",
            'text': "This is another message",
            'timestamp': 1505104583,
            'link': "https://d3n8a8pro7vhmx.cloudfront.net/taxpayers/pages/679/attachments/original/1499663166/4-ways-cheer-up-depressed-cat.jpg",
            'author': 'reza',
            'replyToId': None,
        },
        {
            'id': '113',
            'rawPost': "Anne MSG ** This is a default message",
            'title': "Anne MSG",
            'text': "This is a default message",
            'link': None,
            'timestamp': 1506104583,
            'author': 'anne',
            'replyToId': None,
        },
        {
            'id': '114',
            'rawPost': "ANNE msg 2 ** This is a default message https://www.youtube.com/embed/IvUU8joBb1Q",
            'title': "ANNE msg 2",
            'text': "This is a default message",
            'timestamp': 1506154583,
            'link': "https://www.youtube.com/embed/IvUU8joBb1Q",
            'author': 'anne',
            'replyToId': None,
        },
        {
            'id': '115',
            'rawPost': "Stuff ** Stuff default message",
            'title': "Stuff",
            'text': "Stuff default message",
            'link': None,
            'timestamp': 1506254583,
            'author': 'paul',
            'replyToId': None,
        },
        {
            'id': '116',
            'rawPost': "Stuff 333 ** default message",
            'title': "Stuff 333",
            'text': "default message",
            'link': None,
            'timestamp': 1506204500,
            'author': 'paul',
            'replyToId': None,
        },
        {
            'id': '117',
            'rawPost': "Boo ** boo",
            'title': "Boo",
            'text': "boo",
            'link': None,
            'timestamp': 1516554686,
            'author': 'anne',
            'replyToId': '116'
        },
        {
            'id': '118',
            'rawPost': "Boo Yourself ** boo",
            'title': "Boo Yourself",
            'text': "boo",
            'link': None,
            'timestamp': 1516554886,
            'author': 'paul',
            'replyToId': '117'
        },
        {
            'id': '119',
            'rawPost': "reza",
            'title': "reza",
            'text': "",
            'link': None,
            'timestamp': 1516554986,
            'author': 'reza',
            'replyToId': '118'
        },
        {
            'id': '120',
            'rawPost': "reza reply",
            'title': "reza reply",
            'text': "jfdslkgdjfglk jlkfgjdlkf hjf hlkx",
            'link': None,
            'timestamp': 1516555686,
            'author': 'sara',
            'replyToId': '119'
        },
    ],
    'follows': [
        {
            'follower': "paul",
            'followed': "anne"
        },
        {
            'follower': "paul",
            'followed': "reza"
        },
        {
            'follower': "reza",
            'followed': "anne"
        },
        {
            'follower': "reza",
            'followed': "sara"
        },
        {
            'follower': "reza",
            'followed': "kenn"
        },
    ],
    # '_reposts': [],
    'reposts': [
        {
            'postId': '111',
            'userId': 'reza',
            'timestamp': 1516224583
        },
        {
            'postId': '115',
            'userId': 'anne',
            'timestamp': 1516294583
        },
        {
            'postId': '115',
            'userId': 'paul',
            'timestamp': 1516554583
        },
        {
            'postId': '115',
            'userId': 'kenn',
            'timestamp': 1516554583
        },
        {
            'postId': '115',
            'userId': 'sara',
            'timestamp': 1516554583
        },
    ],
    # '_likes': [],
    'likes': [
        {
            'postId': '112',
            'userId': 'reza',
            'timestamp': 1516224582
        },
        {
            'postId': '113',
            'userId': 'reza',
            'timestamp': 1516254584
        },
        {
            'postId': '113',
            'userId': 'anne',
            'timestamp': 1516294586
        },
        {
            'postId': '113',
            'userId': 'paul',
            'timestamp': 1516554580
        },
        {
            'postId': '115',
            'userId': 'kenn',
            'timestamp': 1516554582
        },
        {
            'postId': '116',
            'userId': 'sara',
            'timestamp': 1516554586
        },
        {
            'postId': '120',
            'userId': 'reza',
            'timestamp': 1516754386
        },
        {
            'postId': '120',
            'userId': 'kenn',
            'timestamp': 1516754586
        },
    ],
}
