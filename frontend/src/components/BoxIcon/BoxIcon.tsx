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
  border?: 'default' | 'circle';
}

const BoxIcon: FC<BoxIconProps> = ({ border, ...props }) => {
  return (
    // @ts-expect-error
    <box-icon border={border === 'circle' ? 'circle' : ''} {...props} />
  );
};

export default BoxIcon;
