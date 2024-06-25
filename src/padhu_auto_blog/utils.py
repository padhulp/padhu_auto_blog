import subprocess

def run_blog_post_script():
    print("Running blog post script...")
    # Your script's main logic here
    result = subprocess.run(['python', 'src/padhu_auto_blog/blog_post.py'], capture_output=True, text=True)
    if result.returncode == 0:
        print("Blog post script executed successfully.")
    else:
        print(f"Blog post script failed with return code {result.returncode}.")
        print(result.stderr)