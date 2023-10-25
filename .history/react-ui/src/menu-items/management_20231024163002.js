// assets
import { IconUser } from '@tabler/icons';

// constant
const icons = {
    IconUser: IconUser
};

//-----------------------|| DASHBOARD MENU ITEMS ||-----------------------//

export const management = {
    id: 'management',
    title: 'Administration',
    type: 'group',
    children: [
        {
            id: 'default',
            title: 'Utilisateur',
            type: 'item',
            url: '/management/user',
            icon: icons['IconUser'],
            breadcrumbs: false
        }
    ]
};
