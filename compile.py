import os
import base64

def compile_project():
    print("Starting compilation...")
    
    # Paths
    html_path = "index.html"
    css_path = "style.css"
    js_path = "app.js"
    output_single = "index_single.html"
    output_blogger = "blogger_base64_embed.html"
    
    if not os.path.exists(html_path) or not os.path.exists(css_path) or not os.path.exists(js_path):
        print("Error: Missing index.html, style.css, or app.js!")
        return
        
    # Read files
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()
        
    # Inject CSS
    css_tag = f'<style>\n{css}\n</style>'
    html = html.replace('<link rel="stylesheet" href="style.css">', css_tag)
    
    # Inject JS
    js_tag = f'<script>\n{js}\n</script>'
    html = html.replace('<script src="app.js"></script>', js_tag)
    
    # Write index_single.html
    with open(output_single, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully compiled {output_single} ({len(html)} bytes)")
    
    # Create Blogger base64 embed
    b64_data = base64.b64encode(html.encode("utf-8")).decode("utf-8")
    iframe_code = f'<iframe src="data:text/html;base64,{b64_data}" width="100%" height="800px" style="border:none; border-radius:18px; box-shadow:0 8px 30px rgba(0,0,0,0.08);" allow="autoplay; microphone"></iframe>'
    
    with open(output_blogger, "w", encoding="utf-8") as f:
        f.write(iframe_code)
    print(f"Successfully generated {output_blogger} ({len(iframe_code)} bytes)")
    print("Compilation completed!")

if __name__ == "__main__":
    compile_project()
