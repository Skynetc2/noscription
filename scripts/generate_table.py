import pandas as pd

def generate_html_table(file_path):
    # Load data from the CSV file
    df = pd.read_csv(file_path)

    # Convert DataFrame to an HTML table
    html_table = df.to_html(index=False, classes='display', table_id='noscriptionTable', escape=False)

    # Complete HTML page with DataTables integration and retro styling
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Find Alternatives to Subscription-Based Services</title>
        <!-- DataTables CSS -->
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.css">
        <!-- Custom CSS for retro styling -->
        <style>
            body {{
                font-family: "Courier New", Courier, monospace;
                background-color: #000;
                color: #0f0;
                margin: 20px;
            }}
            h1 {{
                text-align: center;
                color: #0f0;
            }}
            #noscriptionTable_wrapper {{
                margin-top: 20px;
            }}
            table.dataTable {{
                border: 2px solid #0f0;
                border-collapse: collapse;
                width: 100%;
            }}
            table.dataTable thead th {{
                background-color: #333;
                color: #0f0;
                text-align: center;
                border-bottom: 2px solid #0f0;
            }}
            table.dataTable tbody tr {{
                background-color: #111;
                color: #0f0;
            }}
            table.dataTable tbody tr.odd {{
                background-color: #222;
            }}
            table.dataTable tbody tr:hover {{
                background-color: #555;
            }}
            #noscriptionTable_filter input {{
                margin-left: 5px;
                border-radius: 4px;
                border: 1px solid #0f0;
                padding: 5px;
                background-color: #000;
                color: #0f0;
            }}
            .filter-container {{
                margin-bottom: 20px;
                text-align: center;
            }}
            select {{
                background-color: #000;
                color: #0f0;
                border: 1px solid #0f0;
                padding: 5px;
                margin-right: 10px;
            }}
            footer {{
                margin-top: 20px;
                text-align: center;
                color: #0f0;
            }}
            a {{
                color: #0ff;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
        <!-- jQuery -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <!-- DataTables JS -->
        <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.js"></script>
    </head>
    <body>
        <h1>Find Alternatives to Subscription-Based Services</h1>

        <!-- Filter Dropdowns -->
        <div class="filter-container">
            <label for="typeFilter">Filter by Type:</label>
            <select id="typeFilter">
                <option value="">All Types</option>
                <option value="Subscription">Subscription</option>
                <option value="Proprietary">Proprietary</option>
                <option value="Open Source">Open Source</option>
            </select>
        </div>

        {html_table}

        <!-- Initialize DataTables -->
        <script>
            $(document).ready(function() {{
                var table = $('#noscriptionTable').DataTable({{
                    "paging": true,
                    "searching": true,
                    "ordering": true,
                    "columnDefs": [
                        {{ "width": "15%", "targets": 0 }},
                        {{ "width": "10%", "targets": 1 }},
                        {{ "width": "10%", "targets": 2 }},
                        {{ "width": "15%", "targets": 3 }},
                        {{ "width": "15%", "targets": 4 }},
                        {{ "width": "20%", "targets": 5 }},
                        {{ "width": "15%", "targets": 6 }}
                    ],
                    "language": {{
                        "search": "Filter records:"
                    }}
                }});

                // Filter event handler
                $('#typeFilter').on('change', function() {{
                    var type = $(this).val();
                    table.column(4).search(type).draw();  // Filter by the "Alternative Type" column
                }});
            }});
        </script>

        <footer>
            <p>View this project on <a href="https://github.com/Skynetc2/noscription" target="_blank">GitHub</a>.</p>
        </footer>
    </body>
    </html>
    """

    # Save HTML content to file
    with open('docs/index.html', 'w') as f:
        f.write(html_content)

# Run the function to generate the HTML table
generate_html_table('data/services.csv')
