from pathlib import Path
import pandas as pd
from taipy.gui import Gui, notify
import taipy.gui.builder as tgb

# file_name = input("Enter the file name(Sensitive do upper cases): ")
# sheet_name = input("Enter the sheet name(Sensitive do upper cases): ")
# rows_skipped = int(input("Enter the number of rows to skip(In case there is a title): "))
# columns_start = input("Starts in wich column?: ").upper()
# columns_end = input("Ends in wich column?: ").upper()
# rows = int(input("Enter the number of rows to read: "))

# this_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# wb_file_path = this_dir / "data" / f"{file_name}.xlsx"



data = pd.read_excel(
    io="supermarket_sales.xlsx",#For the sake of the project, I will use the same file
    engine="openpyxl",
    sheet_name="Sales",
    skiprows=3,
    usecols="B:R",
    nrows=1000,
)
# Add 'hour' column to dataframe
data["hour"] = pd.to_datetime(data["Time"], format="%H:%M:%S").dt.hour


# Get unique values of each filter
cities = list(data["City"].unique())
customer_types = list(data["Customer_type"].unique())
genders = list(data["Gender"].unique())


layout = {
    "xaxis": {"title": ""},
    "yaxis": {"title": ""},
    "margin": {"l": 150},
}


def on_filter(state):
    if (
        len(state.cities) == 0
        or len(state.customer_types) == 0
        or len(state.genders) == 0
    ):
        notify(state, "Error", "No results found. Check the filters.")
        return

    state.data_filtered, state.sales_by_product_line, state.sales_by_hour = filter(
        state.cities, state.customer_types, state.genders
    )


def filter(cities, customer_types, genders):
    # Filter the data based on the user selections
    data_filtered = data[
        data["City"].isin(cities)
        & data["Customer_type"].isin(customer_types)
        & data["Gender"].isin(genders)
    ]

    # Calculate sales by product line, summing up the "Total" for each product line, and sorting the results
    sales_by_product_line = (
        data_filtered[["Product line", "Total"]]
        .groupby(by="Product line")
        .sum()
        .sort_values(by="Total", ascending=True)
        .reset_index()  # Converts the "Product line" index into a column
    )

    # Calculate sales by hour, summing up the "Total" for each hour
    sales_by_hour = (
        data_filtered[["hour", "Total"]]
        .groupby(by="hour")
        .sum()
        .reset_index()  # Converts the "hour" index into a column
    )

    # Return the filtered dataset, sales by product line, and sales by hour
    return data_filtered, sales_by_product_line, sales_by_hour


def to_text(value):
    return "{:,}".format(int(value))


with tgb.Page() as page:
    tgb.toggle(theme=True)
    tgb.text("📊 Sales Dashboard", class_name="h1 text-center pb2")

    with tgb.layout("1 1 1", class_name="p1"):
        with tgb.part(class_name="card"):
            tgb.text("## Total Sales:", mode="md")
            tgb.text("US $ {to_text(data_filtered['Total'].sum())}", class_name="h4")

        with tgb.part(class_name="card"):
            tgb.text("## Average Sales:", mode="md")
            tgb.text("US $ {to_text(data_filtered['Total'].mean())}", class_name="h4")

        with tgb.part(class_name="card"):
            tgb.text("## Average Rating:", mode="md")
            tgb.text(
                "{round(data_filtered['Rating'].mean(), 1)}"
                + "{'⭐' * int(round(data_filtered['Rating'].mean()))}",
                class_name="h4",
            )

    with tgb.layout("1 1 1", class_name="p1"):
        tgb.selector(
            value="{cities}",
            lov=cities,
            dropdown=True,
            multiple=True,
            label="Select cities",
            class_name="fullwidth",
            on_change=on_filter,
        )
        tgb.selector(
            value="{customer_types}",
            lov=customer_types,
            dropdown=True,
            multiple=True,
            label="Select customer types",
            class_name="fullwidth",
            on_change=on_filter,
        )
        tgb.selector(
            value="{genders}",
            lov=genders,
            dropdown=True,
            multiple=True,
            label="Select genders",
            class_name="fullwidth",
            on_change=on_filter,
        )

    with tgb.layout("1 1"):
        tgb.chart(
            "{sales_by_hour}",
            x="hour",
            y="Total",
            type="bar",
            title="Sales by Hour",
            layout=layout,
        )
        tgb.chart(
            "{sales_by_product_line}",
            x="Total",
            y="Product line",
            type="bar",
            orientation="h",
            layout=layout,
            title="Sales by Product Line",
        )


if __name__ == "__main__":
    data_filtered, sales_by_product_line, sales_by_hour = filter(
        cities, customer_types, genders
    )
    Gui(page).run(
        title="Sales Dashboard",
        use_reloader=True,
        debug=True,
        watermark="",
        margin="4em",
        favicon="media/favicon-32x32.png"
    )