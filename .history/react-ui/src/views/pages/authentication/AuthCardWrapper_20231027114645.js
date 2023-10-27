import PropTypes from 'prop-types';
import React from 'react';

// material-ui
import { makeStyles } from '@material-ui/styles';

// project import
import MainCard from './../../../ui-component/cards/MainCard';

// style constant
const useStyles = makeStyles((theme) => ({
    card: {
        maxWidth: '450px',
        '& > *': {
            flexGrow: 1,
            flexBasis: '50%'
        },
        [theme.breakpoints.down('sm')]: {
            margin: '20px'
        },
        [theme.breakpoints.down('lg')]: {
            maxWidth: '400px'
        }
    },
    content: {
        paddingX: theme.spacing(5) + ' !important',
        paddingY: theme.spacing(2),
        [theme.breakpoints.down('lg')]: {
            paddingX: theme.spacing(3) + ' !important'
        }
    }
}));

//-----------------------|| AUTHENTICATION CARD WRAPPER ||-----------------------//

const AuthCardWrapper = ({ children, ...other }) => {
    const classes = useStyles();

    return (
        <MainCard className={classes.card} contentClass={classes.content} {...other}>
            {children}
        </MainCard>
    );
};

AuthCardWrapper.propTypes = {
    children: PropTypes.node
};

export default AuthCardWrapper;
