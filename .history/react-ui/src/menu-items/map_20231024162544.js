// assets
import { IconMap, IconDeviceAnalytics } from '@tabler/icons';

// constant
const icons = {
    IconMap: IconMap,
    IconDeviceAnalytics
};

//-----------------------|| DASHBOARD MENU ITEMS ||-----------------------//

export const management = {
    id: 'map',
    title: 'Carte',
    type: 'group',
    children: [
        {
            id: 'default',
            title: 'Carte',
            type: 'item',
            url: '/map',
            icon: icons['IconUser'],
            breadcrumbs: false
        }
    ]
};
