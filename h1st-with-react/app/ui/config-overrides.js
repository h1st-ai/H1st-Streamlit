/* eslint-disable @typescript-eslint/no-var-requires */
const { override, fixBabelImports, addLessLoader } = require('customize-cra');
const aliyunTheme = require('@ant-design/aliyun-theme');

module.exports = override(
  fixBabelImports('antd', {
    libraryDirectory: 'es',
    style: true,
  }),
  addLessLoader({
    lessOptions: {
      javascriptEnabled: true,
      modifyVars: {
        ...aliyunTheme,
        '@primary-color': '#2241B0',
        '@error-color': '#e01702',

        '@btn-primary-color': '#FFFFFF',
        '@btn-danger-color': '#EB7100',
        '@btn-danger-bg': '#FFE3E3',
        '@btn-danger-border': '#FFE3E3',

        '@btn-ghost-color': '#2241B0',
        '@btn-ghost-bg': '#E5F6F0',
        '@btn-ghost-border': '#E5F6F0',
      },
    },
  })
);
