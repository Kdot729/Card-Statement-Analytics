import {View, StyleSheet} from 'react-native';
import { FontAwesome } from '@expo/vector-icons';
import React from "react";
import { Center } from '../css/main';

const Arrow = (): JSX.Element =>
{
    const Arrow_Size = 15
    const Move_Vertically = 7.5
    const Arrow_Color = "rgb(7, 21, 177)"

    const Arrows = [{Direction: "sort-up", Transalte_Y: Move_Vertically}, 
                    {Direction: "sort-down", Transalte_Y: -Move_Vertically}]

    const Font_Awesome_Arrows = Arrows.map((Arrow) =>
    {
        const Transform = StyleSheet.create({Transform: {transform: `translate(3px, ${Arrow["Transalte_Y"]}px)`}})["Transform"]
        const Direction = Arrow["Direction"]

        return <FontAwesome style={Transform} name={Direction}  
                    size={Arrow_Size} color={Arrow_Color} key={Direction}/>
    })

    return  <View style={Center}>
                {Font_Awesome_Arrows}
            </View>
}

export default Arrow