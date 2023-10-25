// assets
import { IconUser, IconDeviceAnalytics } from '@tabler/icons';

// constant
const icons = {
    IconUser: IconUser,
    IconDeviceAnalytics
};

//-----------------------|| DASHBOARD MENU ITEMS ||-----------------------//

export const management = {
    id: 'management',
    title: 'Administration',
    type: 'group',
    children: [
        {
            id: 'default',
            title: 'User',
            type: 'item',
            url: '/management/user',
            icon: icons['IconUser'],
            breadcrumbs: false
        }
    ]
};
