# An alternate version of htis script generated with Claude AI

import argparse
from pathlib import Path
from python_substack import Substack
import sys
import re

def read_markdown_file(file_path):
    """Read content from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

def extract_title_from_content(content):
    """Extract the title from the markdown content (first h1 heading)."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def prepare_content(content):
    """
    Prepare the content for Substack upload.
    Ensures proper formatting is maintained.
    """
    # Remove the title from the content if it exists as h1
    content = re.sub(r'^#\s+.+\n+', '', content, count=1, flags=re.MULTILINE)
    
    # Ensure proper line breaks
    content = content.replace('\n\n', '\n<br><br>\n')
    
    return content.strip()

def upload_to_substack(api_key, newsletter_id, title, content, draft=True):
    """Upload the content to Substack."""
    try:
        substack = Substack(api_key=api_key)
        
        # Create the post
        response = substack.create_post(
            newsletter_id=newsletter_id,
            title=title,
            body=content,
            is_draft=draft
        )
        
        return response
    except Exception as e:
        print(f"Error uploading to Substack: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Upload Markdown file to Substack')
    parser.add_argument('file', help='Path to the markdown file')
    parser.add_argument('--api-key', required=True, help='Substack API key')
    parser.add_argument('--newsletter-id', required=True, help='Substack newsletter ID')
    parser.add_argument('--title', help='Post title (optional, will use first H1 heading if not provided)')
    parser.add_argument('--publish', action='store_true', help='Publish immediately (default is draft)')
    
    args = parser.parse_args()
    
    # Read the markdown file
    content = read_markdown_file(args.file)
    
    # Get the title
    title = args.title or extract_title_from_content(content)
    if not title:
        print("Error: No title provided and couldn't find H1 heading in content")
        sys.exit(1)
    
    # Prepare content
    prepared_content = prepare_content(content)
    
    # Upload to Substack
    response = upload_to_substack(
        api_key=args.api_key,
        newsletter_id=args.newsletter_id,
        title=title,
        content=prepared_content,
        draft=not args.publish
    )
    
    if response:
        status = "published" if not args.publish else "drafted"
        print(f"Successfully {status} post to Substack: '{title}'")
    else:
        print("Failed to upload post to Substack")

if __name__ == "__main__":
    main()
