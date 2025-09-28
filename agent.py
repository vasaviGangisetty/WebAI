from playwright.sync_api import sync_playwright

def search_google(query, top_n=5):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # or False to see browser
        page = browser.new_page()
        page.goto("https://www.google.com")
        
        # Accept cookies if prompted
        try:
            page.locator("text=I agree").click(timeout=2000)
        except:
            pass
        
        page.fill("input[name='q']", query)
        page.keyboard.press("Enter")
        page.wait_for_selector("div#search")
        
        items = page.query_selector_all("div#search .g")
        for it in items[:top_n]:
            title = it.query_selector("h3").inner_text() if it.query_selector("h3") else None
            link = it.query_selector("a").get_attribute("href") if it.query_selector("a") else None
            snippet = it.query_selector(".aCOpRe").inner_text() if it.query_selector(".aCOpRe") else None
            results.append({"title": title, "link": link, "snippet": snippet})
        
        browser.close()
    return results
