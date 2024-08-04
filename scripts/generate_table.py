import pandas as pd

def generate_html_table(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Convert DataFrame to HTML table
    html_table = df.to_html(index=False, classes='table table-striped', border=0)

    # Add search functionality using JavaScript
    search_script = """
    <script>
    function searchTable() {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById('searchInput');
        filter = input.value.toUpperCase();
        table = document.getElementById('dataTable');
        tr = table.getElementsByTagName('tr');
        for (i = 1; i < tr.length; i++) {
            tr[i].style.display = 'none';
            td = tr[i].getElementsByTagName('td');
            for (var j = 0; j < td.length; j++) {
                if (td[j]) {
                    txtValue = td[j].textContent || td[j].innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = '';
                        break;
                    }
                }
            }
        }
    }
    </script>
    """

    # Complete HTML page
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Noscription Alternatives</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}
            th {{
                padding-top: 12px;
                padding-bottom: 12px;
                text-align: left;
                background-color: #f2f2f2;
            }}
            #searchInput {{
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>Noscription Alternatives</h1>
        <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="Search for services...">
        {html_table}
        {search_script}
    </body>
    </html>
    """

    # Save HTML content to file
    with open('docs/index.html', 'w') as f:
        f.write(html_content)

# Run the function to generate the HTML table
generate_html_table('data/services.csv')
