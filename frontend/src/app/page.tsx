"use client"

import { useState } from "react";

export default function Home() {
  interface Driver {
    position: number;
    number: number;
    abbreviation: string;
    full_name: string;
    team_name: string;
  }

  const [drivers, setDrivers] = useState<Driver[]>([]);
  const [year, setYear] = useState<string>("2024");
  const [gp, setGp] = useState<string>("Monza");
  const [session, setSession] = useState<string>("R");
  const [loading, setLoading] = useState<boolean>(false);

  return (
    <main className="flex flex-col items-center p-8 space-y-6">
      <h1 className="text-3xl font-bold">Paddock View</h1>
      
      <div className="flex flex-row gap-4">
        {/* Year Selector */}
        <select
          value={year}
          onChange={(e) => setYear(e.target.value)}
          className="border p-2"
        >
          <option value="2018">2018</option>
          <option value="2019">2019</option>
          <option value="2020">2020</option>
          <option value="2021">2021</option>
          <option value="2022">2022</option>
          <option value="2023">2023</option>
          <option value="2024">2024</option>
          <option value="2025">2025</option>
        </select>

        {/* GP Selector */}
        <select
          value={gp}
          onChange={(e) => setGp(e.target.value)}
          className="border p-2"
        >
          <option value="Melbourne">Melbourne</option>
          <option value="Shanghai">Shanghai</option>
          <option value="Suzuka">Suzuka</option>
          <option value="Sakhir">Sakhir</option>
          <option value="Jeddah">Jeddah</option>
          <option value="Miami">Miami</option>
          <option value="Imola">Imola</option>
          <option value="Monaco">Monaco</option>
          <option value="Barcelona">Barcelona</option>
          <option value="Montreal">Montreal</option>
          <option value="Spielberg">Spielberg</option>
          <option value="Silverstone">Silverstone</option>
          <option value="Spa">Spa</option>
          <option value="Budapest">Budapest</option>
          <option value="Zandvoort">Zandvoort</option>
          <option value="Monza">Monza</option>
          <option value="Baku">Baku</option>
          <option value="Marina Bay">Marina Bay</option>
          <option value="Austin">Austin</option>
          <option value="Mexico City">Mexico City</option>
          <option value="Sao Paulo">Sao Paulo</option>
          <option value="Las Vegas">Las Vegas</option>
          <option value="Lusail">Lusail</option>
          <option value="Yas Island">Yas Island</option>
        </select>

        {/* Session Selector */}
        <select
          value={session}
          onChange={(e) => setSession(e.target.value)}
          className="border p-2"
        >
          <option value="FP1">First Practice</option>
          <option value="FP2">Second Practice</option>
          <option value="FP3">Third Practice</option>
          <option value="Q">Qualifying</option>
          <option value="R">Race</option>
          <option value="S">Sprint</option>
          <option value="SQ">Sprint Qualifying</option>
          <option value="SS">Sprint Shootout</option>
        </select>
      </div>

      {/* Fetch Drivers Button */}
      <button
        disabled={loading}
        onClick={() => {
          setLoading(true);
          fetch(`http://127.0.0.1:8000/drivers?year=${year}&gp=${gp}&session=${session}`)
            .then(res => res.json())
            .then((data: Driver[]) => {
              setDrivers(data);
              setLoading(false);
            })
            .catch(err => {
              console.error(err);
              setLoading(false);
            });
        }}
        className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
      >
        {loading ? "Loading..." : "Fetch Drivers"}
      </button>

      {/* Drivers List */}
      <ul className="mt-6 space-y-2">
        {drivers.map((driver, index) => (
          <li key={index}>
            {driver.position}. {driver.full_name} ({driver.abbreviation}) {driver.number} - {driver.team_name}
          </li>
        ))}
      </ul>
    </main>
  );
}