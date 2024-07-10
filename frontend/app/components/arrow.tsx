import {View, StyleSheet} from 'react-native';
import { FontAwesome } from '@expo/vector-icons';
import React, { createRef, useRef } from "react";
import { Center } from '../css/main';
import { useDispatch, useSelector } from 'react-redux';
import { Sorted, Unsorted } from '@/scripts/redux/sort';

const Arrow = ({Column}): JSX.Element =>
{
    //Note There's 2 createRef because each column has 2 arrows
    const Column_Ref = useRef([createRef(), createRef()]);

    const { value } = useSelector((state) => state["Sorting"])
    const Dispatch = useDispatch()

    const Arrow_Size = 24
    const Move_Vertically = 11
    const Arrow_Color = "rgb(7, 21, 177)"

    const Arrows = [{Direction: "sort-up", Transalte_Y: Move_Vertically, Sort: "Ascending"}, 
                    {Direction: "sort-down", Transalte_Y: -Move_Vertically, Sort: "Descending"}]

    const Font_Awesome_Arrows = Arrows.map((Arrow, Index) =>
    {
        const Transform = StyleSheet.create({Transform: {transform: `translate(3px, ${Arrow["Transalte_Y"]}px)`}})["Transform"]
        const Direction = Arrow["Direction"]

        const Ref = Column_Ref.current[Index]
        const Sort = () => Dispatch(Sorted(Ref.current.props.id))
        
        const ID = `${Column}-${Arrow["Sort"]}`

        return <FontAwesome id={ID} key={ID} ref={Ref} style={Transform} name={Direction}  
                    size={Arrow_Size} color={Arrow_Color} onPress={Sort}/>
    })

    return  <View style={Center}>
                {Font_Awesome_Arrows}
            </View>
}

export default Arrow
