import {View, StyleSheet} from 'react-native';
import React from "react";
import Table_Date from './date';
import { Center, Margin } from '@/scripts/css/main';
import Table_Flatlist from './flatlist';

export const Table = () =>
{
    const Container_Styles = [Flex, Center]
    return  <View style={Container_Styles}>
                <Table_Date />
                <View style={Margin(3)}>
                    <Table_Flatlist />
                </View>
            </View>
}

const Flex = StyleSheet.create(
{
    Container: {flex: 1},
})["Container"]