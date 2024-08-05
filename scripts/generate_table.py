import pandas as pd

def generate_html_table(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Convert DataFrame to HTML table (without styling, DataTables will handle it)
    html_table = df.to_html(index=False, classes='display', table_id='noscriptionTable', escape=False)

    # Complete HTML page with DataTables integration
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Find Alternatives to Subscription-Based Services</title>
        <!-- DataTables CSS -->
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.css">
        <!-- Custom CSS for styling -->
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f8f9fa;
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            #noscriptionTable_wrapper {{
                margin-top: 20px;
            }}
            table.dataTable thead th {{
                background-color: #6c757d;
                color: white;
                text-align: center;
            }}
            table.dataTable tbody tr {{
                background-color: white;
            }}
            table.dataTable tbody tr.odd {{
                background-color: #f2f2f2;
            }}
            #noscriptionTable_filter input {{
                margin-left: 5px;
                border-radius: 4px;
                border: 1px solid #ced4da;
                padding: 5px;
            }}
            footer {{
                margin-top: 20px;
                text-align: center;
                color: #666;
            }}
        </style>
        <!-- jQuery -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <!-- DataTables JS -->
        <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.js"></script>
    </head>
    <body>
        <h1>Find Alternatives to Subscription-Based Services</h1>
        {html_table}
        <!-- Initialize DataTables -->
        <script>
            $(document).ready(function() {{
                $('#noscriptionTable').DataTable({{
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
