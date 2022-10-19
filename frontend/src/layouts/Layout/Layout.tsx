import React, { FC } from 'react';

import Navbar from '@/layouts/Navbar';

export interface LayoutProps {
  children?: React.ReactNode;
}

const Layout: FC<LayoutProps> = ({ children }) => {
  return (
    <>
      <Navbar />
      <main>{children}</main>
    </>
  );
};

export default Layout;
