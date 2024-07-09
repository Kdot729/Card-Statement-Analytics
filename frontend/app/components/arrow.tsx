import {View, StyleSheet} from 'react-native';
import { FontAwesome } from '@expo/vector-icons';
import React, { useRef } from "react";
import { Center } from '../css/main';
import { useDispatch, useSelector } from 'react-redux';
import { Ascending, Descending, Unsorted } from '@/scripts/redux/sort';

const Sort_Ascending = () => 
{

}

const Sort_Descending = () => 
{

}


const Arrow = ({Column}): JSX.Element =>
{
    const Column_Ref = useRef(null)
    const { value } = useSelector((state) => state["Sorting"])
    const Dispatch = useDispatch()

    const Arrow_Size = 24
    const Move_Vertically = 10.5
    const Arrow_Color = "rgb(7, 21, 177)"

    const Dispatching = (Sort_Function) => Dispatch(Sort_Function(Column_Ref.current.props.id))

    const Arrows = [{Direction: "sort-up", Transalte_Y: Move_Vertically, Sort: "Ascending", Press: () => Dispatching(Ascending)}, 
                    {Direction: "sort-down", Transalte_Y: -Move_Vertically, Sort: "Descending", Press: () => Dispatching(Descending)}]

    const Font_Awesome_Arrows = Arrows.map((Arrow) =>
    {
        const Transform = StyleSheet.create({Transform: {transform: `translate(3px, ${Arrow["Transalte_Y"]}px)`}})["Transform"]
        const Direction = Arrow["Direction"]
        const Sort = Arrow["Press"]
        const ID = `${Column}-${Arrow["Sort"]}`

        return <FontAwesome id={ID} key={ID} ref={Column_Ref} style={Transform} name={Direction}  
                    size={Arrow_Size} color={Arrow_Color} onPress={Sort}/>
    })

    return  <View style={Center}>
                {Font_Awesome_Arrows}
            </View>
}

export default Arrow
