// assets
import { IconMap, IconChartArea, IconDeviceAnalytics } from '@tabler/icons';

// constant
const icons = {
    IconMap: IconMap,
    IconChart: IconChartArea,
    IconDeviceAnalytics
};

//-----------------------|| DASHBOARD MENU ITEMS ||-----------------------//

export const visual = {
    id: 'map',
    title: 'Visualisation',
    type: 'group',
    children: [
        {
            id: 'carte',
            title: 'Carte',
            type: 'item',
            url: '/visual/map',
            icon: icons['IconMap'],
            breadcrumbs: false
        },
        {
            id: 'grahic',
            title: 'Graphique',
            type: 'item',
            url: '/visual/graph',
            icon: icons['IconChart'],
            breadcrumbs: false
        }
    ]
};
