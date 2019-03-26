<div class="header_bar">
    <div class="logo_container"><a href="/librarian/{{user_id}}/home">
        <img id='logo' src="/static/images/library_logo.png"> 
        <h1>The Library</h1>
    </a></div>
    <div class ="search_container">
        <form action="/librarian/{{user_id}}/search" method="POST" class="search_bar">
            <input type="search" id="search_input" name="search_query">
            <button type="submit" id="search_button">Search</button>
        </form>
    </div>
</div>