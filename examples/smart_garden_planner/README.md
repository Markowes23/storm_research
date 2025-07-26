# Smart Garden Planner Example

This example demonstrates a small web-based garden planner that recommends plants and watering schedules based on climate and rainfall information. It uses a sample plant database (`plant_data.json`).

## Usage

Launch the Streamlit interface:

```bash
streamlit run web_app.py
```

For command line usage you can still run:

```bash
python garden_planner.py --climate temperate --sunlight "full sun" --soil loamy --rainfall 5
```

Both interfaces will display recommended plants and a simple watering schedule adjusted for weekly rainfall.
