import React, { useEffect, useState } from "react";
import axios from "axios";
import OilPriceChart from "./components/OilPriceChart";
import EventHighlight from "./components/EventHighlight";

function App() {
  // State to store oil price data and events
  const [oilPrices, setOilPrices] = useState([]);
  const [events, setEvents] = useState([]);

  // Fetch oil price data from the Flask backend API
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/oil-prices"
        );
        const dates = response.data.dates;
        const prices = response.data.prices;

        // Format data for the chart
        const formattedData = dates.map((date, index) => ({
          date,
          price: prices[index],
        }));
        setOilPrices(formattedData);
      } catch (error) {
        console.error("Error fetching oil prices:", error);
      }
    };

    fetchData();
  }, []);

  // Simulated events data (can be replaced with an API call)
  useEffect(() => {
    const simulatedEvents = [
      {
        date: "2023-01-01",
        description: "Geopolitical conflict in Region X",
        impact: "Price spike by 5%",
      },
      {
        date: "2023-02-15",
        description: "Economic sanctions imposed",
        impact: "Price drop by 3%",
      },
      {
        date: "2023-03-10",
        description: "OPEC production cut announced",
        impact: "Price increase by 7%",
      },
    ];
    setEvents(simulatedEvents);
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Brent Oil Price Analysis Dashboard</h1>

      {/* Oil Price Chart */}
      <h2>Historical Brent Oil Prices</h2>
      <OilPriceChart data={oilPrices} />

      {/* Event Highlight Section */}
      <h2>Highlighted Events</h2>
      <EventHighlight events={events} />
    </div>
  );
}

export default App;
