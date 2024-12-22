# DataLoom

## Overview
This project transforms Excel data into an interactive dashboard using Python's pandas and Taipy GUI. It allows users to filter sales data based on city, customer type, and gender, providing insightful visualizations of sales by product line and sales by hour.

## Dashboard Demo
![DataLoom](images/DataLoom_demo.gif)

## Installation

### Prerequisites
- Python 3.12+ (Feel free to change the python version in pyproject.toml, just make sure it is compatible with all dependencies)
- [Poetry](https://python-poetry.org/docs/#installation)

### Steps
1. **Clone the repository**
    ```
    git clone https://github.com/CodeZobac/excel-into-interactive-dashboard.git
    cd excel-into-interactive-dashboard
    ```

2. **Install dependencies using Poetry**
    ```
    poetry install
    ```

3. **Activate the Poetry shell**
    ```
    poetry shell
    ```

## Usage
1. **Prepare your Excel file**
    - Place your Excel file in the root directory or specify a different path.

2. **Run the dashboard**
    ```
    python main.py
    ```

3. **Access the dashboard**
    - Open the provided local URL in your web browser to interact with the dashboard.

## Customizing the Excel File
For the sake of the project, a sample Excel file (`supermarket_sales.xlsx`) is used. To use your own Excel file, modify the following lines in `main.py` (lines 18 to 25):

```python
data = pd.read_excel(
    io="your_custom_file.xlsx",
    engine="openpyxl",
    sheet_name="YourSheetName",
    skiprows="Rows skipped if you have any titles",
    usecols="Start Column A : End Column",
    nrows=your_number_of_rows_to_read,
)
```
Adjust the parameters according to the structure of your Excel file to ensure proper data loading and visualization.

## License

MIT License

Copyright (c) 2024 Afonso Caboz

Permission is hereby granted, free of charge, to any person obtaining a copy \
of this software and associated documentation files (the "Software"), to deal \
in the Software without restriction, including without limitation the rights \
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell \
copies of the Software, and to permit persons to whom the Software is \
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all \
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS \
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR \
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER \
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN \
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

