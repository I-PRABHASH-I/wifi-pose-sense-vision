
import React from 'react';
import { NavLink } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Home, Upload, Info, Menu } from 'lucide-react';

interface MainSidebarProps {
  collapsed: boolean;
  setCollapsed: (collapsed: boolean) => void;
}

const MainSidebar: React.FC<MainSidebarProps> = ({ collapsed, setCollapsed }) => {
  return (
    <aside 
      className={`fixed left-0 top-0 z-20 h-full bg-sidebar transition-all duration-300 ease-in-out
      ${collapsed ? 'w-16' : 'w-64 md:w-72'}`}
    >
      <div className="flex h-full flex-col">
        <div className="flex h-16 items-center justify-between px-4 py-4">
          {!collapsed && (
            <div className="flex items-center space-x-2">
              <div className="flex h-6 w-6 items-center justify-center rounded-md bg-sidebar-primary">
                <span className="text-sm font-bold text-white">W</span>
              </div>
              <h1 className="text-lg font-bold text-sidebar-foreground">WiFi-Sense</h1>
            </div>
          )}
          <Button 
            variant="ghost" 
            size="icon" 
            className={`rounded-full ${collapsed ? 'mx-auto' : ''}`}
            onClick={() => setCollapsed(!collapsed)}
          >
            <Menu className="h-5 w-5 text-sidebar-foreground" />
          </Button>
        </div>
        <nav className="mt-4 flex-1 space-y-1 px-3">
          <NavLink 
            to="/"
            className={({ isActive }) => 
              `flex items-center px-2 py-3 text-sidebar-foreground rounded-md transition-all
              ${isActive ? 'bg-sidebar-accent font-medium' : 'hover:bg-sidebar-accent/50'}`
            }
          >
            <Home className="h-5 w-5 mr-3" />
            {!collapsed && <span>Home</span>}
          </NavLink>
          <NavLink 
            to="/prediction"
            className={({ isActive }) => 
              `flex items-center px-2 py-3 text-sidebar-foreground rounded-md transition-all
              ${isActive ? 'bg-sidebar-accent font-medium' : 'hover:bg-sidebar-accent/50'}`
            }
          >
            <Upload className="h-5 w-5 mr-3" />
            {!collapsed && <span>Prediction Tool</span>}
          </NavLink>
          <NavLink 
            to="/about"
            className={({ isActive }) => 
              `flex items-center px-2 py-3 text-sidebar-foreground rounded-md transition-all
              ${isActive ? 'bg-sidebar-accent font-medium' : 'hover:bg-sidebar-accent/50'}`
            }
          >
            <Info className="h-5 w-5 mr-3" />
            {!collapsed && <span>About</span>}
          </NavLink>
        </nav>
        <div className="p-4">
          {!collapsed && (
            <div className="rounded-md bg-sidebar-accent p-3 text-xs text-sidebar-foreground">
              <p className="font-medium">WiFi-Powered Detection</p>
              <p className="mt-1 opacity-80">Human Presence & Pose</p>
            </div>
          )}
        </div>
      </div>
    </aside>
  );
};

export default MainSidebar;
