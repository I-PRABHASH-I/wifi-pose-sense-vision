
import React from 'react';
import { Wifi } from 'lucide-react';

const TopBar: React.FC = () => {
  return (
    <header className="bg-primary text-primary-foreground py-4 px-6 shadow-md">
      <div className="container flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <Wifi className="h-6 w-6" />
          <h1 className="text-xl font-bold">Human Detection through walls using Wi-Fi Signals</h1>
        </div>
      </div>
    </header>
  );
};

export default TopBar;
