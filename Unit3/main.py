# You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

# A post is considered valid if:

# Every opening tag has a corresponding closing tag of the same type.
# Tags are closed in the correct order.

# CREDIT: 

def is_valid_post_format(posts):
    # ()[]{}
    # Tokens to look out for
    tokens = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    stack = []
    
    for c in posts:
        # 
        
        if c in tokens:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                a = stack.pop()
                
                if tokens[a] != c:
                    return False
                
    return True

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

# True
# True
# False


# On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
    stack = []
    
    # 
    while comments:
        c = comments.pop()
        stack.append(c)
        
    return stack
        
# Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
# Example Output:

# ['Thanks for sharing.', 'Love it!', 'Great post!']
# ['Well written.', 'Interesting read.', 'First!']
