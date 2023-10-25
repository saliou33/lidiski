// assets
import { IconMap, IconChartArea } from '@tabler/icons';

// constant
const icons = {
    IconMap: IconMap,
    IconChart: IconChartArea,
};

//-----------------------|| DASHBOARD MENU ITEMS ||-----------------------//

export const visual = {
    id: 'map',
    title: 'Visualisation',
    type: 'group',
    children: [
        {
            id: 'map',
            title: 'Carte',
            type: 'item',
            url: '/visual/map',
            icon: icons['IconMap'],
            breadcrumbs: false
        },
        {
            id: 'chart',
            title: 'Graphique',
            type: 'item',
            url: '/visual/chart',
            icon: icons['IconChart'],
            breadcrumbs: false
        }
    ]
};
