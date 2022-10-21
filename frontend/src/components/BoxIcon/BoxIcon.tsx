import React, { FC } from 'react';

/**
 * These props base on https://boxicons.com/usage#styling
 */
interface BoxIconProps {
  name: string;
  size?: 'xs' | 'sm' | 'md' | 'lg';
  rotate?: '90' | '180' | '270';
  flip?: 'horizontal' | 'vertical';
  pull?: 'left' | 'right';
}

const BoxIcon: FC<BoxIconProps> = (props) => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  return <box-icon {...props} />;
};

export default BoxIcon;
