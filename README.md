# Substack Uploader

**Substack Uploader** is a command-line tool for uploading Markdown posts to your Substack newsletter with ease. It supports draft and published posts, custom titles, and preserves your Markdown formatting.

A Python script that demonstrates how to programmatically create and publish posts on Substack using the Substack API.

## Prerequisites

- Python 3.x
- `substack` Python package
- Substack account credentials

## Environment Variables

The script requires the following environment variables to be set:

- `EMAIL`: Your Substack account email
- `PASSWORD`: Your Substack account password

## Features

The script demonstrates how to:

- Connect to the Substack API
- Switch between different publications
- Create posts with various content types:
  - Regular paragraphs
  - Bold text
  - Hyperlinks
  - Images (both remote and local)
  - Embedded publications
- Set paywall boundaries
- Manage post sections
- Create drafts and publish posts

## Usage Example

### Set up your environment variables first

export EMAIL="your-email@example.com"
export PASSWORD="your-password"

### Run the script
`python substack_upload.py`

## Content Types Demonstrated

1. Basic paragraph text
2. Formatted text (bold)
3. Hyperlinks
4. Paywall placement
5. Remote images
6. Local images
7. Publication embeds
8. Section assignment

## Notes

- The script will create a draft first and then publish it
- Section assignment can only be done after the draft is created
- Make sure you have the necessary permissions for the publication you're posting to
- Images must be accessible and in a supported format

# README - subtstack_upload-V2

## Usage

Run the script from the command line:

```bash
python substack_upload.py path/to/your/post.md --api-key YOUR_API_KEY --newsletter-id YOUR_NEWSLETTER_ID
```

### Additional Options

- `--title "Your Title"`  
  Specify a custom title for your post. If not provided, the script uses the first H1 heading in the Markdown file.

- `--publish`  
  Publish the post immediately. By default, posts are created in draft mode.

---

### Features

The script provides the following functionality:

- **Reads and preserves Markdown formatting**  
  Ensures the original formatting of your post is maintained.

- **Automatically extracts titles from H1 headings**  
  Saves you from manually specifying a title if it's included in the content.

- **Handles proper line breaks**  
  Keeps your text layout as intended.

- **Error handling**  
  Provides robust feedback in case of upload issues.

- **Creates drafts or published posts**  
  Flexible output modes to suit your workflow.

---

### Example Usage

Create and publish a post:

```bash
python substack_upload.py my_post.md --api-key sk_12345 --newsletter-id abc123 --publish
```

Create a draft with a custom title:

```bash
python substack_upload.py my_post.md --api-key sk_12345 --newsletter-id abc123 --title "My Custom Title"
```

---

Feel free to open an issue if you need clarification or additional features!