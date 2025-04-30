
import React, { useState } from 'react';
import { SidebarProvider } from '@/components/ui/sidebar';
import MainSidebar from './MainSidebar';
import { Outlet } from 'react-router-dom';

const AppLayout: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <SidebarProvider>
      <div className="flex min-h-screen w-full bg-background">
        <MainSidebar collapsed={collapsed} setCollapsed={setCollapsed} />
        <main className={`flex-1 transition-all duration-300 ease-in-out ${collapsed ? 'ml-16' : 'ml-64 md:ml-72'}`}>
          <div className="container px-4 py-6 md:px-6 md:py-8">
            <Outlet />
          </div>
        </main>
      </div>
    </SidebarProvider>
  );
};

export default AppLayout;
