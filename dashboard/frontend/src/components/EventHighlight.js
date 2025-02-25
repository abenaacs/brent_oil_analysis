import React from "react";

function EventHighlight({ events }) {
  return (
    <div
      style={{
        padding: "20px",
        backgroundColor: "#f9f9f9",
        border: "1px solid #ddd",
      }}
    >
      <h3>Highlighted Events</h3>
      <ul>
        {events.map((event, index) => (
          <li key={index}>
            <strong>{event.date}</strong>: {event.description} - Impact:{" "}
            {event.impact}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EventHighlight;
