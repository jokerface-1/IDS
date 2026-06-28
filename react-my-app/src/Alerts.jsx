import { useState, useEffect } from "react";
import "./Alerts.css";

function Alerts() {

    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        fetch("http://localhost:3000/data")
            .then(res => res.json())
            .then(data => {
                setAlerts(data);
            });
    }, []);

    return (
        <div className="container">

            <h1 className="title">IDS Dashboard</h1>

            <table className="alertTable">

                <thead>
                    <tr>
                        <th>Source IP</th>
                        <th>Attack</th>
                        <th>Severity</th>
                    </tr>
                </thead>

                <tbody>

                    {alerts.map((alert, index) => (

                        <tr >

                            <td>{alert.ip}</td>

                            <td>{alert.attack}</td>

                            <td>

                                <span className={`badge ${alert.sevierity.toLowerCase()}`}>
                                    {alert.sevierity}
                                </span>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}

export default Alerts;