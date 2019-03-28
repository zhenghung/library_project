<html>
    <head>
        <title>Library 
            % if defined('subtitle'):
            | {{subtitle}}
            % end
        </title>
        <link rel="stylesheet" type="text/css" href="/static/style/global.css">
    </head>
    <body>
        <div class="column" id="left_column">
            % include('user_pages/user_header_bar.tpl')
            <div class="main_page">
                {{!base}}
            </div>
        </div>
        <div class="column" id="right_column">
            % include('user_pages/user_sidebar.tpl')
        </div>
    </body>

</html>