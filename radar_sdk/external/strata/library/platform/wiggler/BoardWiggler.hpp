/**
 * @copyright 2018 Infineon Technologies
 *
 * THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
 * KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
 * PARTICULAR PURPOSE.
 */

#pragma once

#include <platform/BoardDescriptor.hpp>


class BoardWiggler
{
public:
    static std::unique_ptr<BoardDescriptor> searchBoard(uint8_t systemIndex, BoardData::const_iterator begin, BoardData::const_iterator end);
    static std::unique_ptr<BoardInstance> createBoardInstance(uint8_t systemIndex);
};
