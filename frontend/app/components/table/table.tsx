import {View} from 'react-native';
import React from "react";
import Table_Date from './date';
import { Center, Flex } from '@/scripts/css/main';
import Table_Flatlist from './flatlist';

export const Table = () =>
{
    const Container_Styles = [Flex(1), Center]
    return  <View style={Container_Styles}>
                <Table_Date />
                <Table_Flatlist />
            </View>
}