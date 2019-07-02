- DateSelector
    - Search Box
    - Dropdown
    - Selected Items

    interactions:
        - Dropdown returns results as we enter queries into Search Box
        - Clicking on result tries to add it to Selected Items
            - Maybe close dropdown, show loading item in Selected Items
            - If selected item returns no matches, maybe show alert and remove it from Selected Items

- Graph
    - Monthly High/Low
    - Current Temperature

MVP

            January February
Place Name    hi/low
Current Temperature  69

State: {
    ui: {
        SelectedItems: [cid],
        PendingItems: [cid]
    },
    data: {
        [cid]: {
            name: location selected from dropdown; this is from google; will not map to something in database,
            ...database info
        }
    }
}

API
    - Search Text (text)
        - return list of locations matching search query
        - Use Google for this; ideally use lat, lng for place
    - Search Location (lat, lng)
        - returns result closest to point
        - if closest point is more than ten miles away from query, return nothing
        - enhance data with current weather information


    - Search for item by parameter
        - (lat, long) -> returns closest station to lat long
            - should check distance -- if more than 10 miles away return no result
        - (zipcode) -> returns matches for zipcode
            - can we match to closest zipcode?
            - return first match if multiple stations in same zipcode

    - Location:
        - (id) -> return item for id
        - enhance station data with current temperature
